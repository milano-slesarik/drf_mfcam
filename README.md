# ModelFieldChoicesActionMixin

This package is a mixin for Django REST Framework's `ModelViewSet`, which adds a new action `/choices/` that returns a list of values and labels for the choices of a specified model field.

## Usage

Inherit it on your `ModelViewSet`, for example:

```python
class MyModelViewSet(ModelFieldChoicesActionMixin, ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

In a **GET** request to the endpoint `/choices/`, you can specify the field you want the choices for by including the field name as a query parameter, like so:

```
GET .../choices/?field=my_field
```

The response is a list of dictionaries, with each dictionary containing a **"value"** and **"label"**.