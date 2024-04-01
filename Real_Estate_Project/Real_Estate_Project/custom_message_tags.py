from django.contrib.messages import constants as messages

messages.DEFAULT_TAGS.update({
    messages.ERROR: 'danger',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.INFO: 'info',
    messages.DEBUG: 'secondary',
})