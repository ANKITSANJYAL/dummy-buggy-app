class InternalAPIConfig:
    API_GATEWAY_PORT = 8081  # Updated from 8080 to 8081 as per AD-204

    AUTH_SERVICE_URL = f"http://localhost:{API_GATEWAY_PORT}/auth"
    USER_SERVICE_URL = f"http://localhost:{API_GATEWAY_PORT}/users"
    ACTIVITY_SERVICE_URL = f"http://localhost:{API_GATEWAY_PORT}/activity"
    # Add any other service URLs that depend on API_GATEWAY_PORT here

    @classmethod
    def get_service_url(cls, service_name):
        service_map = {
            'auth': cls.AUTH_SERVICE_URL,
            'users': cls.USER_SERVICE_URL,
            'activity': cls.ACTIVITY_SERVICE_URL,
            # Ensure all services are included in the map
        }
        return service_map.get(service_name, None)

    @classmethod
    def get_config(cls):
        return {
            'api_gateway_port': cls.API_GATEWAY_PORT,
            'auth_service_url': cls.AUTH_SERVICE_URL,
            'user_service_url': cls.USER_SERVICE_URL,
            'activity_service_url': cls.ACTIVITY_SERVICE_URL,
            # Include all relevant configuration details
        }