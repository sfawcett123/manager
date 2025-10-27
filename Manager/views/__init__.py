def register_views(app):
    from .home import home
    from .simulator import SimulatorRoutes
    
    home(app)       # Call the home function to register the routes
    SimulatorRoutes(app)  # Call the simulator function to register the routes