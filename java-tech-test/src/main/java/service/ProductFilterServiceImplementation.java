package service;

import model.Product;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class ProductFilterServiceImplementation implements ProductFilterService
{

    @Override
    public Collection<Product> filterProductsByName(Collection<Product> products, String name)
    {
        Collection<Product> Byname = new ArrayList<>();
        for (Product el: products)
        {
            if(el.getName()==name){
                Byname.add(el);
            }
        }
        return Byname;
    }

    @Override
    public Collection<Product> filterProductsByField(Collection<Product> products, String field, String value)
    {
        Collection<Product> Bycategory = new ArrayList<>();
        for (Product el: products)
        {
            switch (field){
                case "category":
                    if (el.getCategory() == value) {
                        Bycategory.add(el);
                    }
                    break;
                case "name":
                    if(el.getName()==value){
                        Bycategory.add(el);
                    }
                    break;
                case "price":
                    if(String.valueOf(el.getPrice())==value){
                        Bycategory.add(el);
                    }
                    break;
            }
        }
        return Bycategory;
    }
}
