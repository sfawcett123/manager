def register_views(app):
    from .home import HomeRoutes
    from .simulator import SimulatorRoutes
    
    HomeRoutes(app)       # Call the home function to register the routes
    SimulatorRoutes(app)  # Call the simulator function to register the routes