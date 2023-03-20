import dropbox

def create_dbx_client(oauth2_access_token):
    return dropbox.Dropbox(
        oauth2_access_token=oauth2_access_token,
        app_key='4k4kxmph890eh78',
        app_secret='64lqv52bd6l64fp'
    )

def check_and_refresh_access_token(dbx):
    try:
        dbx.users_get_current_account()
    except dropbox.exceptions.AuthError as e:
        if e.error.is_expired():
            # atualiza o token de acesso
            oauth2_access_token = dbx.oauth2_token(params=None).access_token
            dbx = create_dbx_client(oauth2_access_token)
            return dbx
    return dbx