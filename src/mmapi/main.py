from imp import reload
from mmapi.app import createApp
import uvicorn

app = createApp()

if __name__ == '__main__':
    Popen(['python', '-m', 'https_redirect'])
    uvicorn.run(app, port=443, host='0.0.0.0', reload=True, reload_dirs=['/workspace'], ssl_keyfile='/etc/letsencrypt/live/lordlabs.club/privkey.pem', ssl_certfile='/etc/letsencrypt/live/lordlabs.club/fullchain.pem')