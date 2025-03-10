import json
from http.server import BaseHTTPRequestHandler, HTTPServer

USERS_LIST = [
    {
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]
USERS_KEYS = {"username", "firstName", "lastName", "email", "password"}
USERS_KEYS_POST = {"id", "username", "firstName", "lastName", "email", "password"}


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200, body=None):
        """
        Procedure with methods
        :param status_code: 100 - 500
        :param body: body of response
        :return: None
        """
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode("utf-8"))

    def _pars_body(self):
        """
        content_length -> Gets the size of data
        :return: Gets the data itself
        """
        content_length = int(self.headers["Content-Length"])
        return json.loads(self.rfile.read(content_length).decode("utf-8"))

    def do_GET(self):
        # test_get_all_users
        if self.path == "/users":
            self._set_response(status_code=200, body=USERS_LIST)

        # test_get_user_by_username
        elif self.path == "/user/theUser":
            self._set_response(status_code=200, body=USERS_LIST[0])

        # test_get_user_by_username_not_found
        elif self.path == "/user/User_not_found":
            self._set_response(status_code=400, body={"error": "User not found"})
        else:
            self._set_response(418)

    def do_POST(self):
        if self.path == "/user":
            body = self._pars_body()

            # test_create_user_duplicate_id
            if body in USERS_LIST:
                self._set_response(status_code=400, body={})

            # test_create_user
            elif set(body.keys()) == USERS_KEYS_POST:
                self._set_response(status_code=201, body=body)

            # test_create_user_not_valid_data
            else:
                self._set_response(status_code=400, body={})

        elif self.path == "/user/createWithList":
            body = self._pars_body()

            # test_create_user_duplicate_id
            if body[0] in USERS_LIST or body[1] in USERS_LIST:
                self._set_response(status_code=400, body={})

            # test_create_users
            elif body[1] not in USERS_LIST:
                self._set_response(status_code=201, body=body)

            # test_create_user_not_valid_data
            else:
                self._set_response(status_code=400, body={})

    def do_PUT(self):
        if self.path == "/user/theUser":
            body = self._pars_body()
            # test_update_user
            if set(body.keys()) == USERS_KEYS:
                USERS_LIST.extend(body)
                self._set_response(status_code=200, body=dict(**body, id=1))

            # test_update_user_not_valid_data
            elif set(body.keys()) != USERS_KEYS:
                self._set_response(
                    status_code=400, body={"error": "not valid request data"}
                )

        # test_update_user_not_found
        elif self.path == "/user/user_not_found":
            self._set_response(status_code=404, body={"error": "User not found"})

    def do_DELETE(self):
        id_1 = 1
        id_22 = 22

        # test_delete_by_id
        if self.path == f"/user/{id_1}":
            self._set_response(status_code=200, body={})

        # test_delete_by_not_valid_id
        elif self.path == f"/user/{id_22}":
            self._set_response(status_code=404, body={"error": "User not found"})
        else:
            self._set_response(status_code=418, body=None)


def run(
    server_class=HTTPServer,
    handler_class=SimpleHTTPRequestHandler,
    host="localhost",
    port=8000,
):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == "__main__":
    from sys import argv

    run(host="localhost", port=8765)
    # if len(argv) =8= 2:
    #     run(port=int(argv[1]))
    # else:
    #     run()
