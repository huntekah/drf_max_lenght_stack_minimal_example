# drf_max_lenght_stack_minimal_examplei

* Failed attempts could be seen at experiment-n-\* branches
* Working solutions from [tiki](https://stackoverflow.com/users/11972800/tiki) and from [Melvyn](https://stackoverflow.com/users/1600649/melvyn) are located on solutions-{user} branches.

About solutions:
* Tiki solution works for serializer, but fails to provide correct message for model. It was not a requirement of an original question, but it is worth mentioning.
* Melvyn solution works both for serializer and model errors.


> Apparently the ModelSerializer doesn't copy the error_messages attribute
> from the model field, so we have to do that by hand.
> - Melvyn
