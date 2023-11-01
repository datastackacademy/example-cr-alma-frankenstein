from flask import Flask, request

data_file = '../data/watson.txt'
fp = None


def read_line():
    global fp, data_file
    if not fp:
        fp = open(data_file, 'r', encoding='utf-8')
    line = fp.readline()
    if line is not None:
        line = line.rstrip('\n\r ')
    return line


app = Flask(__name__)


@app.route("/")
def watson():
    msg = request.args.get('msg', default=None)
    print(f"watson heard: {msg}")
    # finish the rest of this code
    # read the response from the file
    # send the response back in plain text, make sure you get the response header content type for plain text


if __name__ == "__main__":
    # run flask app on port 5050
    app.run('0.0.0.0', 8081)
