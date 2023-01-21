from django.core.exceptions import FieldDoesNotExist
from rest_framework.decorators import action
from rest_framework.response import Response


class ModelFieldChoicesActionMixin:
    """
    Mixin that adds the 'choices' action to the ModelViewSet.
    The action returns a list of values and labels of the choices of a specified model field.

    Usage: /choices/?field=my_field

    Response:

    [
        {
            "value": "choice_a",
            "label": "Choice A"
        },
        {
            "value": "choice_b",
            "label": "Choice B"
        },
        {
            "value": "choice_c",
            "label": "Choice C"
        }...
    ]
    """

    @action(methods=["get"], detail=False, url_path="choices")
    def choices(self, request):
        fieldname = request.GET.get("field")
        Model = self.queryset.model

        try:
            field = Model._meta.get_field(fieldname)
        except FieldDoesNotExist:
            return Response(status=400, data={
                "error": f"The field '{fieldname}' does not exist in model '{Model._meta.model_name}'."})

        if not field.choices:
            return Response(status=400, data={
                "error": f"The field '{fieldname}' in model '{Model._meta.model_name}' has no choices."})

        """
        Returns the choices and labels of the my_field field
        """

        choices = [{"value": value, "label": label} for value, label in field.choices]

        return Response(choices)
