class ProductMapper:
    '''
        Object mapped to class
    '''
    
    def mapper(form):
        '''Maps the request object to a class object.

        Parameters:
            form (form):Request values object.

        Returns:
            JSON: Object mapped to class.   
        '''

        return {
            'name': form['FormName'],
            'price': form['FormPrice']
            }
