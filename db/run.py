from db.faker_generator import generate_electronic_data
from db.operations import create_table_electronics, insert_data


def main():
    create_table_electronics()
    df_fake = generate_electronic_data(n=2751)
    insert_data(df_fake)


if __name__ == "__main__":
    main()
