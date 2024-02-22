## Overview

| Developed by | Guardrails AI |
| --- | --- |
| Date of development | Feb 15, 2024 |
| Validator type | Format |
| Blog | - |
| License | Apache 2 |
| Input/Output | Output |

## Description

This validator ensures that a generated string ends with an expected text. This validator works on strings or lists.

## Installation

```bash
$ guardrails hub install hub://guardrails/ends_with
```

## Usage Examples

### Validating string output via Python

In this example, we apply the validator to a string generated by an LLM.

```python
# Import Guard and Validator
from guardrails.hub import EndsWith
from guardrails import Guard

# Initialize Validator
val = EndsWith(
    end='dog',
    on_fail="fix"
)

# Setup Guard
guard = Guard.from_string(
    validators=[val, ...],
)

guard.parse("My favorite animal is a dog")  # Validator passes
guard.parse("My favorite animal is a cat")  # Validator fails
```

### Validating a string field within a generated JSON

In this example, we apply the validator to a string field of a generated JSON output by an LLM.

```python
# Import Guard and Validator
from pydantic import BaseModel
from guardrails.hub import EndsWith
from guardrails import Guard

# Initialize Validator
val = EndsWith(
    end='dog',
    on_fail="fix"
)

# Create Pydantic BaseModel
class PetInfo(BaseModel):
    pet_name: str
    pet_type: str = Field(
        description="Type of pet", validators=[val]
    )

# Create a Guard to check for valid Pydantic output
guard = Guard.from_pydantic(output_class=PetInfo)

# Run LLM output generating JSON through guard
guard.parse("""
{
    "pet_name": "Caesar",
    "pet_type": "golden retriever dog"
}
""")
```

### Validating a list field within a generated JSON

In this example, we apply the validator to a list field of a generated JSON output by an LLM.

```python
# Import Guard and Validator
from pydantic import BaseModel
from guardrails.hub import EndsWith
from guardrails import Guard

# Initialize Validator
val = EndsWith(
    end=['quick read', 'all'],
    on_fail="fix"
)

class Article(BaseModel):
    """Info about article."""
    title: str = Field(description
    tags: list[str] = Field(
        description="Tags that describe the article",
        validators=[val]
    )

# Create a Guard to check for valid Pydantic output
guard = Guard.from_pydantic(output_class=Article)

# Run LLM output generating JSON through guard
guard.parse("""
{
    "title": "The LLM Infra Stack",
    "tags": ["infra", "ai", "quick read", "all"]
}
""")
```


## API Reference

**`__init__(self, on_fail="noop")`**
<ul>

Initializes a new instance of the Validator class.

**Parameters:**

- **`end`** _(Union[str, list])_: The expected end to the string or list. For strings, this should be a string. For lists, this should either be a list, or a single scalar which will be contained in a list.
- **`on_fail`** *(str, Callable):* The policy to enact when a validator fails. If `str`, must be one of `reask`, `fix`, `filter`, `refrain`, `noop`, `exception` or `fix_reask`. Otherwise, must be a function that is called when the validator fails.

</ul>

<br>

**`__call__(self, value, metadata={}) → ValidationResult`**

<ul>

Validates the given `value` using the rules defined in this validator, relying on the `metadata` provided to customize the validation process. This method is automatically invoked by `guard.parse(...)`, ensuring the validation logic is applied to the input data.

Note:

1. This method should not be called directly by the user. Instead, invoke `guard.parse(...)` where this method will be called internally for each associated Validator.
2. When invoking `guard.parse(...)`, ensure to pass the appropriate `metadata` dictionary that includes keys and values required by this validator. If `guard` is associated with multiple validators, combine all necessary metadata into a single dictionary.

**Parameters:**

- **`value`** *(Any):* The input value to validate.
- **`metadata`** *(dict):* A dictionary containing metadata required for validation. No additional metadata keys are needed for this validator.

</ul>
