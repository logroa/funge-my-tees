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
            hex: ''
        };
        // will add functionality for picking shirt
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
            hex: shirt_rep.hex
        });
    };

    render() {
        const { id, name, pic1_img_url, pic1_title, pic2_img_url, pic2_title, price, available, hex } = this.state;

        let p1_url = "../src/images/".concat(pic1_img_url);
        let p2_url = "../src/images/".concat(pic2_img_url);

        const shirtstyle = {
            backgroundColor: hex
        }

        return (
            <div className='shirt' style={shirtstyle}>
                <div className='shirttext'>
                    <p>{name}</p>
                    <p>${price}</p>
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
                </div>
            </div>
        );
    }
}

Shirt.propTypes = {
    shirt_rep: PropTypes.object.isRequired,
};

export default Shirt;