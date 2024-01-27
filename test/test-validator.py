from guardrails import Guard
from pydantic import BaseModel, Field
from validator import EndsWith


class ValidatorTestObject(BaseModel):
    test_val: list = Field(
        validators=[
            EndsWith(end="c", on_fail="exception")
        ]
    )


TEST_OUTPUT = """
{
  "test_val": ["a", "b", "c"]
}
"""


guard = Guard.from_pydantic(output_class=ValidatorTestObject)

raw_output, guarded_output, *rest = guard.parse(TEST_OUTPUT)

print("validated output: ", guarded_output)


TEST_FAIL_OUTPUT = """
{
"test_val": ["a", "b"]
}
"""

try:
  guard.parse(TEST_FAIL_OUTPUT)
  print ("Failed to fail validation when it was supposed to")
except (Exception):
  print ('Successfully failed validation when it was supposed to')