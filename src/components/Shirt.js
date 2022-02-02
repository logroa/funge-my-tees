import React from 'react';
import PropTypes from 'prop-types';
import './Shirt.css';


class Shirt extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            id: 0,
            name: '',
            front_img_url: '',
            back_img_url: '',
            price: 0,
            available: true,
            hex: '',
            form_is_open: false
        };
        // will add functionality for picking shirt
        this.openForm = this.openForm.bind(this);
    }

    componentDidMount() {
        const { shirt_rep } = this.props;
        this.setState({
            id: shirt_rep.id,
            name: shirt_rep.name,
            pic1_img_url: shirt_rep.pic1_img_url,
            pic1_title: shirt_rep.pic1_title,
            pic2_img_url: shirt_rep.pic2_img_url,
            pic2_title: shirt_rep.pic2_title,
            price: shirt_rep.price,
            available: shirt_rep.available,
            hex: shirt_rep.hex,
            form_is_open: false
        });
    };

    openForm() {
        this.setState({ form_is_open: true });
    }

    orderShirt() {
        
    }

    render() {
        const { id, name, pic1_img_url, pic1_title, pic2_img_url, pic2_title, price, available, hex, form_is_open } = this.state;

        let p1_url = "../src/images/".concat(pic1_img_url);
        let p2_url = "../src/images/".concat(pic2_img_url);

        const shirtstyle = {
            backgroundColor: hex
        }

        function sizeRenderer() {
            let num_shirts = document.getElementById("shirt-num").value
            let size_options = "";
            for (let x = 0; x < parseInt(num_shirts); ++x) {
                size_options += (
                    `<select name="size${x.toString()}" id="shirt-size"  required>
                        <option value="S">S</option>
                        <option value="M">M</option>
                        <option value="L">L</option>
                        <option value="XL">XL</option>
                    </select> <br/>`
                );
            }
            document.getElementById("sizes").innerHTML = size_options
        }

        let form = ""
        if (form_is_open) {
            form = (
                <div id="form">
                    <form id="order-shirt" onSubmit={(event) => this.orderShirt(event)}>
                        Name <input type="text" name="name" required/>
                        Email <input type="text" name="email" required/>
                        Phone Number <input type="text" name="phone_number" required/>
                        How many?   <select name="shirt-num" id="shirt-num" onChange={sizeRenderer()} required>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                        </select>

                        <div id="sizes"></div>

                        <input type="submit" value="Mint"/>
                    </form>
                </div>
            );
        }

        return (
            <div className='shirt' style={shirtstyle}>
                <div className='shirttext'>
                    <p>{name}</p>
                    <p>${price}</p>

                    <button className="form-opener" onClick={() => {this.openForm()}}>
                        Mint Yours
                    </button>
                </div>
                <div className='shirtimages'>
                    <div className='shirtbox'>
                        <img src={p1_url} alt={p1_url} className='shirtpic'/>
                        <p>{pic1_title}</p>
                    </div>
                    <div className='shirtbox'>
                        <img src={p2_url} alt={p2_url} className='shirtpic'/>
                        <p>{pic2_title}</p>
                    </div>

                    {form}
                </div>
            </div>
        );
    }
}

Shirt.propTypes = {
    shirt_rep: PropTypes.object.isRequired,
};

export default Shirt;