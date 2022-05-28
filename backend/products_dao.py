from sql_connection import get_sql_connection

def get_all_products(connection):

	
	cursor =connection.cursor()

	query = ("select products.*,uoms.uom_name from products inner join uoms on products.uom_id = uoms.uom_id")

	cursor.execute(query)

	products = []

	for (product_id, name, uom_id, price_per_unit,uom_name) in cursor:
		products.append({
			'product_id':product_id,
			'name':name,
			'uom_id':uom_id,
			'price_per_unit':price_per_unit,
			'uom_name':uom_name
			})

	return products

def insert_new_product(connection,product):
	cursor = connection.cursor()
	query = "insert into products (product_name,uom_id,price_per_unit) values (%s,%s,%s)"
	data = (product['product_name'],product['uom_id'],product['price_per_unit'])
	cursor.execute(query,data)
	connection.commit()

	return cursor.lastrowid

def delete_product(connection,product_id):
	cursor = connection.cursor()
	query = "delete from products where product_id = "+str(product_id)
	cursor.execute(query)
	connection.commit()


# make module

if __name__ == '__main__':
	connection = get_sql_connection()
	print(get_all_products(connection))
	print(insert_new_product(connection,{
			'product_name':'banana',
			'uom_id':'1',
			'price_per_unit':'5.0',
			}))
	delete_product(connection,1)

# dao = data access object