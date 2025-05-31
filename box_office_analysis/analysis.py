import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        self.data.columns = self.data.columns.str.strip()
        self.data = self.data.dropna(subset=['Rank', '$Worldwide', 'Year'])
        self.data['Rating_Num'] = self.data['Rating'].str.extract(r'(\d+\.\d+)').astype(float)
        return self.data
    
class DataAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe

    def get_statistics(self):
        return {
            "vote_count": {
                "media": self.df['Vote_Count'].mean(),
                "mediana": self.df['Vote_Count'].median(),
                "desvio_padrao": self.df['Vote_Count'].std()
            },
            "rating": {
                "media": self.df['Rating_Num'].mean(),
                "mediana": self.df['Rating_Num'].median(),
                "desvio_padrao": self.df['Rating_Num'].std()
            },
            "worldwide": {
                "media": self.df['$Worldwide'].mean(),
                "mediana": self.df['$Worldwide'].median(),
                "desvio_padrao": self.df['$Worldwide'].std()
            }
        }

    def get_record_by_id(self, id_):
        row = self.df[self.df['Rank'] == id_]
        if row.empty:
            return {"erro": "ID nao encontrado"}
        return row.to_dict(orient='records')[0]
    
    def get_data(self, year_min=None,year_max=None, genre=None, min_rating=None, max_rating=None):
        df = self.df.copy()

        if year_min is not None:
            df = df[df['Year'] >= year_min]
        if year_max is not None:
            df = df[df['Year'] <= year_max]  
        if genre is not None:
            df = df[df['Genres'].str.contains(genre, case=False, na=False)]
        if min_rating is not None:
            df = df[df['Rating_Num'] >= min_rating]
        if max_rating is not None:
            df = df[df['Rating_Num'] <= max_rating]

        columns_to_send = ['Release Group', 'Year', '$Worldwide', 'Rating_Num', 'Rank', 'Vote_Count', 'Rating','$Domestic','$Foreign']
        data = df[columns_to_send].to_dict(orient='records')

        return data
    
    def get_all_category(self):
        genres_series = self.df['Genres'].dropna().str.split(', ')
        genres_list = genres_series.explode().unique().tolist()
        return genres_list
        