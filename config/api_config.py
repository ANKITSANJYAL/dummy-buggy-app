class InternalAPIConfig:
    # Update the port to 8081 as per AD-204
    API_GATEWAY_PORT = 8081

    # Update all service URLs that depend on the API_GATEWAY_PORT
    AUTH_SERVICE_URL = f"http://localhost:{API_GATEWAY_PORT}/auth"
    USER_SERVICE_URL = f"http://localhost:{API_GATEWAY_PORT}/users"
    ACTIVITY_SERVICE_URL = f"http://localhost:{API_GATEWAY_PORT}/activities"

    @staticmethod
    def get_service_url(service_name: str) -> str:
        service_map = {
            'auth': InternalAPIConfig.AUTH_SERVICE_URL,
            'users': InternalAPIConfig.USER_SERVICE_URL,
            'activities': InternalAPIConfig.ACTIVITY_SERVICE_URL
        }
        return service_map.get(service_name, "")

    @staticmethod
    def get_config() -> dict:
        return {
            'API_GATEWAY_PORT': InternalAPIConfig.API_GATEWAY_PORT,
            'AUTH_SERVICE_URL': InternalAPIConfig.AUTH_SERVICE_URL,
            'USER_SERVICE_URL': InternalAPIConfig.USER_SERVICE_URL,
            'ACTIVITY_SERVICE_URL': InternalAPIConfig.ACTIVITY_SERVICE_URL
        }