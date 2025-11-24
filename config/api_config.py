class InternalAPIConfig:
    API_GATEWAY_PORT = 8081  # Updated from 8080 to 8081 as per AD-204

    AUTH_SERVICE_URL = f"http://localhost:{API_GATEWAY_PORT}/auth"
    USER_SERVICE_URL = f"http://localhost:{API_GATEWAY_PORT}/users"
    ACTIVITY_SERVICE_URL = f"http://localhost:{API_GATEWAY_PORT}/activity"

    @classmethod
    def get_service_url(cls, service_name):
        service_map = {
            'auth': cls.AUTH_SERVICE_URL,
            'users': cls.USER_SERVICE_URL,
            'activity': cls.ACTIVITY_SERVICE_URL
        }
        return service_map.get(service_name)

    @classmethod
    def get_config(cls):
        return {
            'API_GATEWAY_PORT': cls.API_GATEWAY_PORT,
            'AUTH_SERVICE_URL': cls.AUTH_SERVICE_URL,
            'USER_SERVICE_URL': cls.USER_SERVICE_URL,
            'ACTIVITY_SERVICE_URL': cls.ACTIVITY_SERVICE_URL
        }