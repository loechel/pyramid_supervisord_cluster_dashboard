from persistent.mapping import PersistentMapping


class BaseModel(PersistentMapping):
    __parent__ = __name__ = None


class LoginModel():
    pass


class LogoutModel():
    pass


class Dashboard():
    pass


def appmaker(zodb_root):
    if 'app_root' not in zodb_root:
        app_root = BaseModel()
        zodb_root['app_root'] = app_root
        import transaction
        transaction.commit()
    return zodb_root['app_root']
