from kor.nodes import Object, Text

def get_schema(schema_type:str):

    organization_schema = Object(
        id="organization",
        description="Information about an social network organization or a group information. An organization comprises one or more people and have a particular purpose.",
        attributes=[
            Text(
                id="organization_name",
                description="The name of an organization.",
                examples=[
                    (
                        "Melbourne University is a university located in Australia.",
                        "Melbourne University",
                    ),
                    (
                        "Mike plays footy with David's footy team every week.",
                        "David's footy team",
                    ),
                ],
            ),
            Text(
                id="organization_location",
                description="The location of an organization.",
                examples=[
                    (
                        "Melbourne University is a university located in Australia.",
                        "Australia",
                    ),
                    (
                        "Mike plays footy with David's footy team every week at Brighton beach.",
                        "Brighton beach",
                    ),
                ],
            ),
        ],
        examples=[
            (
                "Steve Jobs co-founded Apple Inc. along with Steve Wozniak and Ronald Wayne.",
                [("organization_name", "Apple Inc.")],
            ),
            (
                "Sam regularly goes to Melbourne's St. Paul's Cathedral to participate in church activities.",
                [
                    {
                        "organization_name": "church",
                        "organization_location": "Melbourne's St. Paul's Cathedral",
                    },
                ],
            ),
        ],
    )

    person_schema = Object(
        id="person",
        description="Personal information",
        attributes=[
            Text(
                id="first_name",
                description="The first name of a person.",
                examples=[
                    ("Barack Hussein Obama went to an Asian restaurant.", "Barack"),
                    (
                        "Sam Chiang met Donald John Trump at a coffee shop yesterday",
                        ["Sam", "Donald"],
                    ),
                ],
            ),
            Text(
                id="last_name",
                description="The last name of a person.",
                examples=[
                    ("Barack Hussein Obama went to an Asian restaurant.", "Obama"),
                    (
                        "Sam Chiang met Donald Trump at a coffee shop yesterday",
                        ["Chiang", "Trump"],
                    ),
                ],
            ),
            Text(
                id="middle_name",
                description="The middle name of a person.",
                examples=[
                    ("Barack Hussein Obama went to an Asian restaurant.", "Hussein"),
                    (
                        "Sam Chiang met Donald John Trump at a coffee shop yesterday",
                        "John",
                    ),
                ],
            ),
            Text(
                id="nationality",
                description="The nationality of a person.",
                examples=[
                    (
                        "Both Barack Hussein Obama and Donald John Trump, who had served as the Presidents of the United States.",
                        ["American", "American"],
                    )
                ],
            ),
            organization_schema,
        ],
        examples=[
            (
                "Alice and Bob are friends",
                [{"first_name": "Alice"}, {"first_name": "Bob"}],
            ),
            (
                "Sam Chaing visited the White House in Washington, and met both Barack Hussein Obama and Donald John Trump, who had served as the Presidents of the United States.",
                [
                    {
                        "first_name": "Barack",
                        "last_name": "Obama",
                        "middle_name": "Hussein",
                        "nationality": "American",
                    },
                    {
                        "first_name": "Donald",
                        "last_name": "Trump",
                        "middle_name": "John",
                        "nationality": "American",
                    },
                    {"first_name": "Sam", "last_name": "Chaing"},
                ],  # nationality induction work?
            ),
            (
                "Steve Jobs co-founded Apple Inc. along with Steve Wozniak and Ronald Wayne.",
                [
                    {
                        "first_name": "Steve",
                        "last_name": "Jobs",
                        "organization": "Apple Inc.",
                    },
                    {
                        "first_name": "Steve",
                        "last_name": "Wozniak",
                        "organization": "Apple Inc.",
                    },
                    {
                        "first_name": "Ronald",
                        "last_name": "Wayne",
                        "organization": "Apple Inc.",
                    },
                ],
            ),
            (
                "Sam Chaing go to a church at Melbourne every week.",
                [
                    {
                        "first_name": "Sam",
                        "last_name": "Chaing",
                        "organization": [
                            {
                                "organization_name": "church",
                                "organization_location": "Melbourne",
                            }
                        ],
                    }
                ],
            ),
        ],
    )
    if schema_type == "organization":
        return organization_schema
    elif schema_type == "person":
        return person_schema
    else:
        return None
