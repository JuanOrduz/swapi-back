from typing import List

from django.db.models import Model


def generic_model_mutation_process(
    model: Model,
    data: dict,
    id: int = None,
    commit: bool = True,
    related_objects: List[int] = None,
) -> Model:
    """
    Updates or creates Django model object.

    :param Model model: Django model class
    :param dict data: Model object data
    :param int id: Object id
    :param bool commit: Save model default True
    :return: django model instance
    """
    if id:
        item = model.objects.get(id=id)
        try:
            del data["id"]
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        item = model(**data)

    if commit:
        item.save()

    if related_objects:
        for key, objects in related_objects.items():
            getattr(item, key).set(objects)

    return item
