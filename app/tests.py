import json

from graphene_django.utils.testing import GraphQLTestCase

from app.models import People
from swapi.schema import schema


class FirstTestCase(GraphQLTestCase):
    fixtures = ["app/fixtures/unittest.json"]
    GRAPHQL_SCHEMA = schema

    def test_people_query(self):
        test_query = """
          query{
            allPlanets {
              edges{
                node{
                  id
                  name
                }
              }
            }
          }
        """
        response = self.query(
            test_query,
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(len(content["data"]["allPlanets"]["edges"]), 61)

    def test_create_people_query(self):
        test_query = """
            mutation {
            createPeopleMutation(input: {
              name: "Captain Rex",
              homeWorld: "YXJyYXljb25uZWN0aW9uOjE=",
              films: [
                "RmlsbVR5cGU6MQ==",
                "RmlsbVR5cGU6Mg==",
                "RmlsbVR5cGU6Mw=="],
            }) {
              people {
                id
                name
                films {
                  edges{
                    node{
                      id
                      title
                    }
                  }
                }
              }
            }
          }
        """
        response = self.query(
            test_query,
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertTrue(
            content["data"]["createPeopleMutation"]["people"]["name"] == "Captain Rex",
        )
        self.assertEqual(
            len(content["data"]["createPeopleMutation"]["people"]["films"]["edges"]),
            3,
        )
        self.assertTrue(People.objects.get(name="Captain Rex"))

    def test_update_people_query(self):
        test_query = """
          mutation {
            updatePeopleMutation(input: {
              id: "UGVvcGxlVHlwZTox",
              skinColor: "pink",
            }) {
              people {
                id
                name
                skinColor
              }
            }
          }
        """
        self.assertEqual(People.objects.get(name="Luke Skywalker").skin_color, "fair")
        response = self.query(
            test_query,
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertTrue(
            content["data"]["updatePeopleMutation"]["people"]["skinColor"] == "pink",
        )
        self.assertEqual(People.objects.get(name="Luke Skywalker").skin_color, "pink")
