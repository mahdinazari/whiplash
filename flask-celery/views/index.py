from flask import jsonify, Blueprint

from tasks import add, mul, say_hello
from application.celery import celery


blueprint = Blueprint('views/index', __name__, url_prefix='/api/v1')


@blueprint.route('/index', methods=['GET'])
def index():
    conf = celery.conf.humanize(censored=True)
    print(conf)

    add_result = add.apply_async([10, 2], propagate=False)
    mul_result = mul.apply_async([10, 0])
    print(add_result.get())
    print("propagate=False is using for ignoren the exceptions")
    print(mul_result.get(propagate=False))

    if mul_result.traceback:
        print(mul_result.traceback)

    # forget is used for ignore the result
    mul_result_1 = mul.apply_async([10, 1])
    mul_result_1.forget()

    # countdown: wait to return response
    # queue: specify queue, celery is default queue
    add_result_0 = add.apply_async([10, 2], countdown=10, queue='celery')
    add_result_0.forget()

    # when forgetting a result countdown is ignoring

    add_result_1 = add.apply_async([10, 2], countdown=10, queue='celery')
    print(add_result_1.state)

    print(add_result_1.id)
    print(add_result_1.state)
    print(celery.AsyncResult(add_result_1.id).successful())
    print(celery.AsyncResult(add_result_1.id).failed())

    # signature
    sign = add.signature((10, 5))
    sign_add_result = sign.delay()
    print(sign_add_result.get())

    mul_result = mul.apply_async([10, 2], countdown=10)
    print(mul_result.get())
    print(add_result_1.get())

    result = say_hello.apply_async(['mehdi'], propagate=False)
    print(result.get())

    if add_result.ready():
        return jsonify("Done")

