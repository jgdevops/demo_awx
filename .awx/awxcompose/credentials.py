DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "awxpass",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "OmFIOlQxdGFORjRBT0lPWmlsY21rMnRnd0c4Tm1PZExvOWFUTmNKVUdkX2N4VnhPSCxWbmVlbkQ6Nmc2VEZsVXB3WDN1Z1Q1alVCRTlLNGVrSkQ3NDVMNGd1R09YSFlBLnlDbkxyN3V2cUVlMXBXb0RGck1ZOFFuLWdZYSxxbzI="
