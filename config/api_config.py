class InternalAPIConfig:
    API_GATEWAY_PORT = 8081  # Updated from 8080 to 8081

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
        return service_map.get(service_name, "")

    @classmethod
    def get_config(cls):
        return {
            'port': cls.API_GATEWAY_PORT,
            'services': {
                'auth': cls.AUTH_SERVICE_URL,
                'users': cls.USER_SERVICE_URL,
                'activity': cls.ACTIVITY_SERVICE_URL
            }
        }