import pandas as pd

class Pipeline_Beckn:
  """
  Class for Beckn data processing pipeline.
  """

  def __init__(self, path_file):
    """
    Initialize the pipeline with the path to the CSV file.

    Args:
    - path_file (str): Path to the CSV file.
    """
    self.path_file = path_file
    self.data = pd.read_csv(self.path_file)

  def preparation_(self):
    """
    Prepare the data for analysis.

    This method performs several cleaning and preprocessing operations on the data.
    """

    # Rename columns
    old_list_rename = ['Nom_du_POI', 'Contacts_du_POI']
    new_list_rename = ['Lieux', 'Contacts_des_lieux']
    self.data.rename(columns=dict(zip(old_list_rename, new_list_rename)), inplace=True)

    # Drop columns
    columns_to_delete = ['Categories_de_POI', 'Periodes_regroupees', 'Covid19_mesures_specifiques',
                             'Createur_de_la_donnee', 'SIT_diffuseur', 'Date_de_mise_a_jour', 'URI_ID_du_POI']
    self.data.drop(columns_to_delete, axis=1, inplace=True)

    # Drop missing observations
    self.data.dropna(subset=['Adresse_postale', 'Contacts_des_lieux'], inplace=True)

    # Operations on Adresse and Code postal columns
    self.data['Code_postal_et_commune'] = self.data['Code_postal_et_commune'].str.replace('#',' ')
    self.data['Adresse'] = self.data['Adresse_postale'] + ', ' + self.data['Code_postal_et_commune']
    self.data.drop(['Adresse_postale', 'Code_postal_et_commune'], axis=1, inplace=True)

    # Operations on Contacts_du_POI column
    self.data['Contacts_des_lieux'] = self.data['Contacts_des_lieux'].str.replace('#',' ')

    # Drop Classements_du_POI column
    self.data.drop('Classements_du_POI', axis=1, inplace=True)

    # Drop rows with missing values in Description column
    self.data.dropna(subset=['Description'], inplace=True)

    # Create a new column containing the combined text
    self.data["text"] = self.data["Adresse"] + self.data["Contacts_des_lieux"] + self.data["Description"]

    # Separate training data and labels
    self.trains = self.data["text"].copy()
    self.labels_name = self.data["Lieux"]

    # Merge data and assign unique IDs
    self.concat_data = pd.concat([self.trains, self.labels_name], axis=1)
    self.concat_data['unique_id'] = range(len(self.concat_data))

    return self.concat_data