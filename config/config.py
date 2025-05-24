from urllib.parse import quote_plus

usuario = "HIA-ADMIN@hia-2025"
password = quote_plus("@dm1n_IA")

CONNECTION_STRING = (
    f"mssql+pyodbc://{usuario}:{password}@hia-2025.database.windows.net:1433/HIA-Project"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&encrypt=yes"
    "&trustServerCertificate=no"
    "&hostNameInCertificate=*.database.windows.net"
    "&loginTimeout=500"
)
