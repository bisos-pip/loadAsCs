#   /bin/env loadAsHashTag.later

__version__ = "1.0"

pyModuleType = "generic"

def genericMain(
        *args,
        **kwargs,
):
    print(f"genericMain(Args):")
    print(f"{args}")
    print(f"genericMain(KWArgs):")
    print(f"{kwargs}")

    for key, value in kwargs.items():
      print(key, "->", value)
    print(f"In moduleMain")


def genericCliParams ():
    return [
        (
        "genericParName",  # parCliName
        "Generic Parameter Name",  # parName
        "Full Description of Parameter Comes Here", # parDescription
        "Int", # parDataType
        22, # parDefault
        [3,22,99] # parChoices
        )
    ]
