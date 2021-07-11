from flask import Blueprint

from application.tasks import add, mul


blueprint = Blueprint('views/practice', __name__, url_prefix='/api/v1/index')


@blueprint.route('/', methods=['GET'])
def index():
    for j in range(0, 20):
        async_add_result = add.apply_async(
            [j, j+2],
            queue='queue3',
            countdown=2
        )
        async_add_get_result = async_add_result.get(propagate=False)
        print(f'run add {j} in queue3 -> {async_add_get_result}')

    for i in range(0, 100):
        add_result = add.delay(i, i+10)
        mul_result = mul.delay(i, i+10)
        add_get_result = add_result.get(propagate=False)
        mul_get_result = mul_result.get(propagate=False)
        print(f"task add result {i} + {i}    is: {add_get_result}")
        print(f"task mul result {i} + {i}    is: {mul_get_result}")

    if add_result.state == 'SUCCESS':
        return 'hello worild! \n'

    else:
        return add_result.traceback()

