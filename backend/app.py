import redis
import random
import config
from flask import Flask, jsonify, request


app = Flask(__name__)

if __name__ == "__main__":
    app.config.from_object("config.DevConfig")
else:
    app.config.from_object("config.Config")

database = redis.Redis(host=app.config["REDIS_HOSTNAME"], port=6379, decode_responses=True)


def generate_code():
    for i in range(10):
        code = str(random.randint(0, 10000)).zfill(4)

        if not database.exists("clipboard:{}".format(code)):
            return code

    while True:
        code = str(random.randint(0, 100000)).zfill(5)

        if not database.exists("clipboard:{}".format(code)):
            return code


@app.route("/clipboard/<string:share_id>", methods=["GET"])
def get_clipboard(share_id):
    if not share_id or len(share_id) > 10:
        return jsonify({"status": "error", "msg": "Invalid Code!"}), 400

    clipboard = database.get("clipboard:{}".format(share_id))

    if clipboard:
        return jsonify({"status": "success", "code": share_id, "clipboard": clipboard})
    else:
        return jsonify({"status": "error", "msg": "Invalid Code!"}), 400


@app.route("/clipboard", methods=["POST"])
def set_clipboard():
    payload = request.get_json(force=True)

    if not payload.get("clipboard"):
        return jsonify({"status": "error", "msg": "No contents in the clipboard!"}), 400

    code = generate_code()

    database.set("clipboard:{}".format(code), payload["clipboard"])
    database.expire("clipboard:{}".format(code), app.config["TIMEOUT"])

    return jsonify({"status": "success", "code": code, "clipboard": payload["clipboard"]})


@app.route("/status", methods=["GET"])
def get_status():
    try:
        info = database.info()
    except:
        return jsonify({"status": "error", "msg": "Couldn't connect to Redis!"}), 500

    return jsonify({"status": "success", "database": {"expired_keys": info["expired_keys"], "used_memory": info["used_memory"], "commands_count": info["total_commands_processed"]}})


@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def error_handler(error):
    return jsonify({"status": "error", "msg": error.description}), error.code


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
