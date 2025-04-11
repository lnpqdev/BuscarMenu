import pandas as pd

def export_to_excel(menus, file_name='menus.xlsx'):
    df = pd.DataFrame(menus)
    df.to_excel(file_name, index=False)