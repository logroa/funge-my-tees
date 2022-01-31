import React from 'react';
import PropTypes from 'prop-types';
import Shirt from './Shirt';
import './Closet.css';


class Closet extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            status: '',
            shirts: [],
            called_url: ''
        }
        // will prob need functionality
    }

    componentDidMount() {
        const { url } = this.props;
        const requestOptions = {
            method: 'GET',
            headers: { 'Content-Type': 'text/javascript'},
            credentials: 'same-origin'
        }
        fetch(url, requestOptions)
            .then((response) => {
                if (!response.ok) throw Error(response.statusText);
                return response.json();
            })
            .then((data) => {
                this.setState({
                    status: data.status,
                    shirts: data.data,
                    called_url: url
                })
            })
            .catch((error) => console.log(error));
    }

    render() {
        const { status, shirts, url } = this.state;

        let rendered_shirts = shirts.map((s) => 
            <div key={s.name}>
                <Shirt shirt_rep={s} />
            </div>
        );

        return (
            <div className='closet'>
                {rendered_shirts}
            </div>
        );
    }
}

Closet.propTypes = {
    url: PropTypes.string.isRequired,
};

export default Closet