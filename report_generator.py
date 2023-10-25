###############################################################
#                                                             #
#                       Report Generator                      #
#                   VERSION 1.0 - 22.10.2023                  #
#                                                             #
#  Author :  Martin LEMAIRE - ERT FD co-TL                    #
#  Contact : martin.lemaire@epfl.ch                           #
#                                                             #
###############################################################
#                                                             #
# Operation Procedure: report_generation_readme.md (MarkDown) #
#                                                             #
###############################################################


# IMPORTS
from fpdf import FPDF
import pandas as pd


# PDF Class definition
# Contains functions to generate specific layouts of the report's components

class PDF(FPDF):

    # Layout of the Logos and Title
    def header(self):
        # Logo
        self.image('report_images/rocket_logo.png', 155, 6, 40)
        self.image('report_images/nordend_logo.png', 20, 9, 33)
        self.set_font('Arial', 'B', 14)
        self.cell(0, 17, 'Nordend Specifications - 23.10.2023', 10, 1, 'C')
        self.set_font('Arial', 'B', 11)
        self.cell(0, 0, 'Flight Dynamics', 10, 1, 'C')
        self.set_font('Arial', 'IU', 11)
        self.cell(0, 12, 'Author: Martin Lemaire', 10, 1, 'C')
        self.ln(30)  # Add space below the title
        self.set_font('Arial', 'B', 12)

    # Layout of the left boxes
    def chapter_box(self, x, y, title, body, graph_path):
        self.set_fill_color(255, 255, 255)
        self.rect(x, y, 90, 115, 'DF')
        self.set_xy(x, y)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 14)
        self.cell(90, 10, title, 1, 1, 'C', 1)
        self.set_font('Arial', '', 7)
        self.set_xy(x, y)
        self.ln(7)
        self.multi_cell(90, 4.5, body)
        if graph_path!="":
            self.image(graph_path, x + 2, self.get_y(), w=88)

    # Layout of the right boxes
    def chapter_box_bis(self, x, y, title, body, graph_path):
        self.set_fill_color(255, 255, 255)
        self.rect(x, y, 90, 115, 'DF')
        self.set_xy(x, y)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 14)
        self.cell(90, 10, title, 1, 1, 'C', 1)
        self.set_font('Arial', '', 7)
        self.set_xy(x, y)
        self.multi_cell(90, 4.5, body)
        if graph_path!="":
            self.image(graph_path, x + 2, self.get_y(), w=85)

    # Layout of the box of the second page
    def simulations_box(self, x, y, title, body, traj_path, acc_path, vel_path , alt_path):
        self.set_fill_color(255, 255, 255)
        self.rect(x, y, 190, 210, 'DF')
        self.set_xy(x, y)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 14)
        self.cell(190, 10, title, 1, 1, 'C', 1)
        self.set_font('Arial', '', 10)
        self.multi_cell(90, 5, body)
        self.ln(8)
        self.image(traj_path, x + 2, self.get_y(), w=85)
        self.image(acc_path, x + 95, self.get_y()+20, w=85)
        self.image(vel_path, x + 2, self.get_y()+100, w=85)
        self.image(alt_path, x + 95, self.get_y()+100, w=85)


if __name__ == "__main__":
    rocket_report = PDF()
    rocket_report.add_page()
    rocket_report.set_left_margin(10)
    rocket_report.set_right_margin(10)

    # Fetch the data of the rocket
    # Centralized in a csv file
    eng = pd.read_csv("report_data.csv")

    # Content of the Engine box
    engine_data = f"""
    Engine Model :         {eng['Values'][2-2]}              | Engine dry mass :    {eng['Values'][3-2]}
    {eng['Values'][4-2]} mass :               {eng['Values'][12-2]}                   | {eng['Values'][6-2]} mass :              {eng['Values'][11-2]}
    Center of dry mass : {eng['Values'][9-2]}                | Nozzle Radius :       {eng['Values'][8-2]}
    Dry inertia :               {eng['Values'][10-2]} | {eng['Values'][4-2]} density (ga-li) : {eng['Values'][5-2]}
    {eng['Values'][6-2]} density (ga-li) :  {eng['Values'][7-2]}          | Burn Time :              {eng['Values'][13-2]}
    Total impulse :           {eng['Values'][14-2]}                    | Peak thrust :            {eng['Values'][15-2]} 
    Average thrust :         {eng['Values'][16-2]} 
    Thurst Curve : """
    rocket_report.chapter_box(10, 50, 'Engine Data', engine_data, eng['Values'][17-2])

    # Content of the Rocket box
    rocket_data = f"""

    
    {eng['Values'][4-2]} tank position :       {eng['Values'][19-2]}      | {eng['Values'][6-2]} tank position : {eng['Values'][18-2]}
    Upper button position : {eng['Values'][20-2]}        | Lower button position : {eng['Values'][21-2]}
    Inertia :          {eng['Values'][22-2]}   | Drag coefficient : {eng['Values'][23-2]}
    Center of mass without motor : {eng['Values'][24-2]} | Engine position : {eng['Values'][25-2]}
    Boat tail top radius : {eng['Values'][26-2]}          | Boat tail bottom radius : {eng['Values'][27-2]}
    Boat tail length : {eng['Values'][28-2]}                  | Boat tail position : {eng['Values'][29-2]}
    Dry mass : {eng['Values'][30-2]}                            | Radius : {eng['Values'][31-2]}
    OpenRocket view : 
    """
    rocket_report.chapter_box_bis(110, 50, 'Rocket Data', rocket_data,eng['Values'][32-2])

    # Content of the Aerodynamics box
    aerodynamics = f"""
    Number of fins :       {eng['Values'][33-2]}
    Fins root chord :      {eng['Values'][34-2]}
    Fins tip chord :        {eng['Values'][35-2]}
    Fins span :              {eng['Values'][36-2]}
    Fins position :          {eng['Values'][37-2]}
    Fins cant angle :       {eng['Values'][38-2]}
    Fins sweep angle :   {eng['Values'][39-2]}
    Nosecone Length :   {eng['Values'][40-2]}
    Nosecone position :  {eng['Values'][41-2]}
    Nosecone type :       {eng['Values'][42-2]}
    """
    rocket_report.chapter_box(10, 172, 'Aerodynamics', aerodynamics,"")

    # Content of the Recovery box
    recovery = f"""


    Drogue drag coefficient : {eng['Values'][43-2]}
    Drogue trigger :                {eng['Values'][44-2]}
    Drogue sampling rate :    {eng['Values'][45-2]}
    Drogue lag :                     {eng['Values'][46-2]}
    Drogue noise :                {eng['Values'][47-2]}
    Main drag coefficient :     {eng['Values'][48-2]}
    Main trigger :                   {eng['Values'][49-2]}
    Main sampling rate :       {eng['Values'][50-2]}
    Main lag :                        {eng['Values'][51-2]}
    Main noise :                    {eng['Values'][52-2]}
    """
    rocket_report.chapter_box_bis(110, 172, 'Recovery', recovery,"")

    rocket_report.add_page()

    # Content of the Simulations box
    simulations = f"""
    Latitude :            {eng['Values'][53-2]}
    Longitude :         {eng['Values'][54-2]}
    Elevation :          {eng['Values'][55-2]}
    Rail length :        {eng['Values'][56-2]}
    Rail inclination :  {eng['Values'][57-2]}
    """
    rocket_report.simulations_box(10, 50, 'Flight Simulations', simulations, eng['Values'][58-2],eng['Values'][59-2],eng['Values'][60-2],eng['Values'][61-2])

    rocket_report.ln(160)
    Units = """
    UNITS  :  [L] = meters / [T] = seconds / [angle] = degrees / [force] = N / [mass] = kg
    """
    rocket_report.cell(190, 10, Units, 1, 1, 'C', 1)

    # Save the PDF report in the folder "results"
    pdf_filename = "results/rocket_report.pdf"
    rocket_report.output(pdf_filename)
    print(f"Rocket report has been generated and saved as {pdf_filename}")