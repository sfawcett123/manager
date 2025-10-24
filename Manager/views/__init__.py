def register_views(app):
    from .home import home
    from .simulator import simulator
    
    home(app)       # Call the home function to register the routes
    simulator(app)  # Call the simulator function to register the routes