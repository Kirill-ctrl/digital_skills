from pprint import pprint

# input
seq = [
    {
        'name': 'Kirill',
        'status': "student"
    },
    (100, 200, 30, 5000, 'type: measure', 'name_measure: rub'),
    'package',
    hex(123123),
    {"product_1", "product_2", "product_3"},
]


# output
# data = {
#     "info": {
#         "name": "Kirill",
#         "status": "student"
#     },
#     "measure_value": {
#         "type": "measure",
#         "name_measure": "rub",
#         "values_to_products": [
#             {
#                 "name": "product_1",
#                 "value": 100,
#             },
#             {
#                 "name": "product_2",
#                 "value": 200,
#             },
#             {
#                 "name": "product_3",
#                 "value": 30,
#             },
#             {
#                 "name": "product_4",
#                 "value": 5000,
#             },
#         ]
#     },
#     "number": hex(123123),
#     "name": "package",
#     "products": ["product_1", "product_2", "product_3"],
#     "all_price": 330
# }

def seq_to_struct_dict(sub: list) -> dict:
    """Отображает последовательность в словарь"""
    result = {}
    if isinstance(sub, dict):
        if list(sub.keys()) == ['name', 'status']:
            result['info'] = {
                'name': sub.get('name'),
                'status': sub.get('status')
            }
            return result
    elif isinstance(sub, tuple):
        type_meas = name_meas = None
        for val in sub:
            if isinstance(val, str):
                if 'type' in val:
                    type_meas = val
                if 'name_measure' in val:
                    name_meas = val
        result['measure_value'] = {
            "type": type_meas.split(': ')[-1] if type_meas else None,
            "name_measure": name_meas.split(': ')[-1] if name_meas else None,
            "values_to_products": [
                {
                    "name": f"product_{i + 1}",
                    "value": s
                }
                for i, s in enumerate(sub) if isinstance(s, int or float)
            ]
        }
        return result
    if isinstance(sub, str):
        if '0x' in sub:
            result['number'] = sub
            return result
        result['name'] = sub
        return result
    if isinstance(sub, set):
        result['products'] = [
            val
            for val in sub
        ]
        return result
    return result


if __name__ == '__main__':
    print("map")
    result_dict = {}
    for item in list(map(lambda x: seq_to_struct_dict(x), seq)):
        result_dict.update(item)
    result_dict['all_price'] = sum(map(lambda x: x.get('value') if x.get('name') in result_dict.get('products') else 0,
                                       result_dict.get('measure_value')['values_to_products']))
    pprint(result_dict)
