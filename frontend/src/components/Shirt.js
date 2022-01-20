import React from 'react'
import PropTypes from 'prop-types'


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
            available: shirt_rep.available
        });
    };

    render() {
        const { id, name, front_img_url, back_img_url, price, available } = this.state;

        let front = "/images/".concat(front_img_url);
        let back = "/images/".concat(back_img_url);

        return (
            <div className='shirt'>
                <p>{name}</p>
                <p>${price}</p>
                <img src={front} alt={front} />
                <img src={back} alt="Back IMG" />
            </div>
        );
    }
}

Shirt.propTypes = {
    shirt_rep: PropTypes.object.isRequired,
};

export default Shirt;