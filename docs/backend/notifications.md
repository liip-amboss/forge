# Notifications

Forge has a base notification class to send HTML emails.

## Email Settings

To configure the eMail settings Forge uses the python package [django-email-url](https://github.com/migonzalvar/dj-email-url).
The following settings can be done via environment variables.

### EMAIL_URL
Used to configure the SMTP server for sending emails. Defaults to `console://` to write emails messages to STDOUT.

### EMAIL_ADMIN
Used to configure the default to address.

### EMAIL_SENDER
Used to configure the default from address.

### EMAIL_BASE_URL
Used to configure the base URL for static files in emails. 
This gets injected in to the context via a custom context processor and is available in all templates with `{{ EMAIL_BASE_URL }}`

## How to use

### Template
Create your own template file and extend it from `{% extends 'email/base.html' %}`.
You can overwrite all the content via these available blocks: `title, stlye, preview_text, logo, content, copyright, company_address`.

If you just need to extend one of the blocks you can overwrite the block and call the super method.
```python
{% block style %}
    ...your code

    {{ block.super }}
    
    ...your code
{% endblock %}
```

### Notification Class
Create an instance of the `ForgeNotification` class and set the class variables to you needs.
Available variables: `subject, recipient, sender, template, context`.

To send the email you can call the `.send()` method.

```python
from notification.mail import ForgeNotification

message = ForgeNotification()
message.sender = 'be-dev@liip.ch'
message.recipient = [email,]
message.subject = 'Forge Test Email'
message.send()
```

For more complex scenarios you can subclass the `ForgeNotification` class and overwrite the desired methods.

## Development
If the app runs in `DEBUG=True` you have to views to test the email:
- `http://api.forge.docker.test/notification/template` to test the template in the browser
- `https://api.forge.docker.test/notification/test?email=YOUR_EMAIL` to send a test email

You can adjust these view to work with your custom template.
