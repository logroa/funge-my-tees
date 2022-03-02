import React from 'react';
import PropTypes from 'prop-types';
import './Shirt.css';


class Shirt extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            id: 0,
            name: '',
            pic1_img_url: '',
            pic1_title: '',
            pic2_img_url: '',
            pic2_title: '',
            price: 0,
            available: true,
            hex: '',
            form_is_open: false,
            order_name: "",
            order_phone_number: "",
            order_email: "",
            num_shirts: 1,
            size_forms: [],
            order_shirts: {}
        };
        // will add functionality for picking shirt
        this.formTypeHandle = this.formTypeHandle.bind(this);
        this.openForm = this.openForm.bind(this);
        this.orderShirt = this.orderShirt.bind(this);
        this.formSelectHandle = this.formSelectHandle.bind(this);
        this.defaultSizeMaker = this.defaultSizeMaker.bind(this);
        this.sizeRenderer = this.sizeRenderer.bind(this);
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
            form_is_open: false,
            num_shirts: 1,
            size_forms: [
                [0, <div>
                    <select name="size0" id="shirt-size" onChange={(event) => this.formSelectHandle(event)} required>
                        <option value="S">S</option>
                        <option value="M">M</option>
                        <option value="L">L</option>
                        <option value="XL">XL</option>
                    </select> <br/>
                </div>]            
            ],
            order_shirts: {"size0": "S"}
        });
    };

    formTypeHandle(field, event) {
        this.setState({ [field]: event.target.value });
    }

    formSelectHandle(event) {
        this.setState(prevState => {
            let shirts = prevState.order_shirts;
            shirts[event.target.name] = event.target.value
            return {
                order_shirts: shirts
            }
        });
    }

    defaultSizeMaker(shirt) {
        this.setState(prevState => {
            let shirts = prevState.order_shirts;
            shirts[shirt] = "S"
            return {
                num_shirts: 1,
                order_shirts: shirts
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
            body: JSON.stringify(
                {
                    "email": this.state.order_email,
                    "name": this.state.order_name,
                    "phone_number": this.state.order_phone_number,
                    "orders": this.state.order_shirts,
                    "order_price": this.state.price,
                    "id": this.state.id
                }
            )
        };
        const api_url = 'http://localhost:8000/api/order/'; //'https://nfteeshirts.herokuapp.com/api/order/';
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
                    num_shirts: 1,
                    size_forms: [
                        [0,<div>
                            <select name="size0" id="shirt-size" onChange={(event) => this.formSelectHandle(event)} required>
                                <option value="S">S</option>
                                <option value="M">M</option>
                                <option value="L">L</option>
                                <option value="XL">XL</option>
                            </select> <br/>
                        </div>]
                    ],
                    order_shirts: {"size0": "S"}                   
                });
            })
            .catch((error) => console.log(error));
        event.preventDefault();
    }

    sizeRenderer() {
        let num_shirts1 = document.getElementById("shirt-num").value
        let size_options = [];
        this.setState({
            num_shirts: parseInt(num_shirts1),
            size_forms: [],
            order_shirts: {}
        });
        for (let x = 0; x < parseInt(num_shirts1); ++x) {
            let num = "size".concat(x.toString())
            size_options.push(
                [x, <div>
                    <select name={num} id="shirt-size" onChange={(event) => this.formSelectHandle(event)} required>
                        <option value="S">S</option>
                        <option value="M">M</option>
                        <option value="L">L</option>
                        <option value="XL">XL</option>
                    </select> <br/>
                </div>]
            );
            this.defaultSizeMaker("size".concat(x.toString()));
        }
        this.setState({
            size_forms: size_options
        });
    }

    render() {
        const { id, name, pic1_img_url, pic1_title, pic2_img_url, pic2_title, price, available, hex, form_is_open,
                order_name, order_phone_number, order_email, num_shirts, size_forms, order_shirts } = this.state;

        let p1_url = "../src/images/".concat(pic1_img_url);
        let p2_url = "../src/images/".concat(pic2_img_url);

        const shirtstyle = {
            backgroundColor: hex
        }

        let buttonstyle = {
            backgroundColor: "#FFFFFF",
            color: hex
        }
        if (hex == "#FFFFFF") {
            let bstyle = {
                backgroundColor: "#000000",
                color: "#FFFFFF"
            }
            buttonstyle = bstyle
        }

        let form = ""
        if (form_is_open) {
            let shirt_sizes = size_forms.map((s) => 
                <li key={s[0]}>{s[1]}</li>
            );

            form = (
                <div id="form">
                    <form id="order-shirt" onSubmit={(event) => this.orderShirt(event)}>
                        Name <input type="text" name="name" onChange={(event) => this.setState({ order_name: event.target.value })} required/> <br/>
                        Email <input type="text" name="email" onChange={(event) => this.setState({ order_email: event.target.value })} required/> <br/>
                        Phone Number <input type="text" name="phone_number" onChange={(event) => this.setState({ order_phone_number: event.target.value })} required/> <br/>
                        How many?   <select name="shirt-num" id="shirt-num" onChange={() => this.sizeRenderer()} required>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                        </select>

                        <div id="sizes">
                            {shirt_sizes}
                        </div>

                        <br/><input className="form-opener" style={buttonstyle} type="submit" value="Mint"/>
                    </form>
                </div>
            );
        }

        return (
            <div className='shirt' style={shirtstyle}>
                <div className='shirttext'>
                    <p>{name}</p>
                    <p>${price}</p>

                    <button className="form-opener" style={buttonstyle} onClick={() => {this.openForm()}}>
                        Mint Yours
                    </button>
                </div>
                <div className='shirtimages'>
                    <div className='imagesonly'>
                        <div className='shirtbox'>
                            <img src={p1_url} alt={p1_url} className='shirtpic'/>
                            <p>{pic1_title}</p>
                        </div>
                        <div className='shirtbox'>
                            <img src={p2_url} alt={p2_url} className='shirtpic'/>
                            <p>{pic2_title}</p>
                        </div>
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