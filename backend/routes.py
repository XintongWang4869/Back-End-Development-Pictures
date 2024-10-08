from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    return jsonify(data)

######################################################################
# GET A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    for picture in data:
        if picture['id'] == id:
            return picture
    return {"message":"Picture not found."}, 404


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    new_pic = request.json
    print(new_pic)
    if not new_pic.get('id'): 
        return {"message":"Invalid input parameter"}, 422
    for picture in data:
        if picture["id"] == new_pic.get('id'):
            return {"Message": f"picture with id {new_pic['id']} already present"}, 302
    try:
        data.append(new_pic)
        return new_pic, 201
    except NameError:
        return {"message": "Data not defined"}, 500
    

######################################################################
# UPDATE A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    update_info = request.json
    for idx, picture in enumerate(data):
        if picture['id'] == id:
            data[idx] = update_info
            return {"Message":"Picture updated"}, 200
    return {"message": "picture not found"}, 404
            

######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    for picture in data:
        if picture['id'] == id:
            data.remove(picture)
            return {},204
    return {"message": "picture not found"}, 404
