import graphene
from graphql_relay import from_global_id  # noqa: WPS347

from app.models import People, Planet
from app.types import PeopleType, PlanetType
from app.utils import generic_model_mutation_process


class UpdateCreatePlanetMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        rotation_period = graphene.String(required=False)
        orbital_period = graphene.String(required=False)
        diameter = graphene.String(required=False)
        climate = graphene.String(required=False)
        gravity = graphene.String(required=False)
        terrain = graphene.String(required=False)
        surface_water = graphene.String(required=False)
        population = graphene.String(required=False)

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get("id", None)

        data = {"model": Planet, "data": input}
        if raw_id:
            data["id"] = from_global_id(raw_id)[1]

        planet = generic_model_mutation_process(**data)
        return UpdateCreatePlanetMutation(planet=planet)


class CreatePeopleMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        height = graphene.String(required=False)
        mass = graphene.String(required=False)
        gender = graphene.Enum("PeopleGenderEnum", People.GENDER)
        hair_color = graphene.Enum("PeopleHairColorEnum", People.HAIR_COLOR)
        skin_color = graphene.String(required=False)
        birth_year = graphene.String(required=False)
        eye_color = graphene.Enum("PeopleEyeColorEnum", People.EYE_COLOR)
        home_world = graphene.ID(required=True)
        films = graphene.List(graphene.ID)

    people = graphene.Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        home_world = input.get("home_world", None)
        films = input.pop("films", None)

        data = {"model": People, "data": input}
        if home_world:
            data["data"]["home_world"] = Planet.objects.get(
                id=from_global_id(home_world)[1],
            )
        if films:
            data["related_objects"] = {
                "films": [from_global_id(film_id)[1] for film_id in films],
            }

        people = generic_model_mutation_process(**data)
        return CreatePeopleMutation(people=people)
