# Task manager

This project realize __task manager__ backend using Django/DRF.

## Models 
There are considered following identities:

- ___User___ <div>
There is used model from `django.contrib.auth.models`.
To split users into developers and managers were used `Group` model from the same package
and data migration for creation related field in the corresponding table.
</div>

- ___Project___ <div>
Nothing specific appears there. Just data field and m2m relation with User model.
</div>

- ___Task___ <div>
Also nothing is interesting

## API
Endpoints:

- Model related:
	- `api/developers/` Data quering in this case is filtered to contain only developers.
	- `api/tasks/`
	- `api/projects/`
- Others
	- `auth/` Endpoint that provide POST-method request to grand _Token_
	- `swagger/` Swagger documentation 

## Notes

It's sad that there isn't carry all clauses out. Specifically:

- __Test cases__ <div>
If test were provided then they were very primitive. The project isn't solve difficult problem and it's silly to provide test cases for simple models and ViewSets. I understand that writing test cases very important in developing good apps. So apologize please it me.
</div>

- __Email notifications__ <div>
I never works with celery and due to late start I haven't had time to learn it.

And I apologize for dirty code. And thanks for attempt be piece of yours dream team.
