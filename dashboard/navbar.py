import dash_bootstrap_components as dbc
from app import config

dashboard_id = config["dashboard_id"]


def navbar():
    """
    Implements the navigation bar that is at the top of the page. New pages need to be first added here, 
    then the link needs to be added to the index.
    For more customization information please see: 
    https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
    """
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink(
                "Seite 1", href=f"/{dashboard_id}/apps/app1", external_link=True)),
            dbc.NavItem(dbc.NavLink(
                "Seite 2", href=f"/{dashboard_id}/apps/app2", external_link=True)),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Dropdown Title", header=True),
                    dbc.DropdownMenuItem("Dropdown 1", href="#"),
                    dbc.DropdownMenuItem("Dropdown 2", href="#"),
                ],
                id="navbar",
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="Example Custom Python Dashboard",
        color="primary",
        dark=True,
    )
    return navbar
