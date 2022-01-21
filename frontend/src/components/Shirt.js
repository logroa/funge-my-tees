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
            front_img_url: shirt_rep.front_img_url,
            back_img_url: shirt_rep.back_img_url,
            price: shirt_rep.price,
            available: shirt_rep.available,
            hex: shirt_rep.hex
        });
    };

    render() {
        const { id, name, front_img_url, back_img_url, price, available, hex } = this.state;

        let front = "/images/".concat(front_img_url);
        let back = "/images/".concat(back_img_url);

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
                        <img src={front} alt={front} className='shirtpic'/>
                        <p>Front</p>
                    </div>
                    <div className='shirtbox'>
                        <img src={back} alt="Back IMG" className='shirtpic'/>
                        <p>Back</p>
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