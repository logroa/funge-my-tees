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
            form_is_open: false,
            order_name: "",
            order_phone_number: "",
            order_email: "",
            order_shirts: []
        };
        // will add functionality for picking shirt
        this.formTypeHandle = this.formTypeHandle.bind(this);
        this.openForm = this.openForm.bind(this);
        this.orderShirt = this.orderShirt.bind(this);
        this.formSelectHandle = this.formSelectHandle.bind(this)
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

    formTypeHandle(field, event) {
        this.setState({ [field]: event.target.value });
    }

    formSelectHandle(event) {
        this.setState(prevState => {
            return {
                order_shirts: prevState.order_shirts.push(event.target.value)
            }
        });
    }

    openForm() {
        if (this.state.form_is_open) {
            this.setState({ form_is_open: false });
        }
        else {
            this.setState({ form_is_open: true})
        }
    }

    orderShirt(event) {
        const newOrder = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            data: JSON.stringify(
                {
                    "email": this.state.order_email,
                    "name": this.state.order_name,
                    "phone_number": this.state.phone_number,
                    "orders": this.state.order_shirts,
                    "order_price": this.state.price,
                    "id": this.state.id
                }
            )
        };
        const api_url = 'https://nfteeshirts.herokuapp.com/api/order/';
        fetch(api_url, newOrder)
            .then((response) => {
                if (!response.ok) throw Error(response.statusText);
                return response.json();
            })
            .then((data) => {
                this.setState({
                    form_is_open: false,
                    order_name: "",
                    order_phone_number: "",
                    order_email: "",
                    order_shirts: []                   
                });
            })
            .catch((error) => console.log(error));
        event.preventDefault();
    }

    render() {
        const { id, name, pic1_img_url, pic1_title, pic2_img_url, pic2_title, price, available, hex, form_is_open,
                order_name, order_phone_number, order_email, order_shirts } = this.state;

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
                    `<select name="size${x.toString()}" id="shirt-size" onChange={(event) => this.formSelectHandle(event)} required>
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
                        Name <input type="text" name="name" onChange={(event) => this.formTypeHandle({order_name}, event)} required/>
                        Email <input type="text" name="email" onChange={(event) => this.formTypeHandle({order_email}, event)} required/>
                        Phone Number <input type="text" name="phone_number" onChange={(event) => this.formTypeHandle({order_phone_number}, event)} required/>
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