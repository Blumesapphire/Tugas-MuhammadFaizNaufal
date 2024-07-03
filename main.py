from flask import Flask, render_template
from project_post import Service, salon_service


salon_service = salon_service
service_object = []
for item in salon_service:
    item_obj = Service(item, salon_service[item])
    service_object.append(item_obj)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", all_service = service_object)

@app.route("/test")
def test():
    return render_template("index2.html", all_service = service_object)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/booking/")
def booking():
    return render_template("booking.html")

@app.route("/service/<index>")
def show_service(index):
    requested_service = None
    for service in service_object:
        if service.type == index:
            requested_service = service
    return render_template("post.html", service=requested_service)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
    # host='localhost', port=5000
