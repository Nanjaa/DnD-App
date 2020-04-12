from flask import Flask, jsonify, abort, request
import datetime
app = Flask(__name__)


campaigns = [
    {
        'id': 1,
        'name': 'Storm Kings Thunder',
        'players': [
            {
                'id': 1,
                'name': 'Stephanie',
                'gm': True,
                'race': None,
                'class': None
            },
            {
                'id': 2,
                'name': 'Justin',
                'gm': False,
                'race': 1,
                'class': 1
            },
            {
                'id': 3,
                'name': 'Mike',
                'gm': False,
                'race': 2,
                'class': 2
            },
            {
                'id': 4,
                'name': 'Michael',
                'gm': False,
                'race': 3,
                'class': 3
            },
            {
                'id': 5,
                'name': 'Kim',
                'gm': False,
                'race': 4,
                'class': 4
            },
            {
                'id': 6,
                'name': 'Brody',
                'gm': False,
                'race': 5,
                'class': 5
            }
        ],
        'start_date': datetime.datetime.now(),
        'status': 1
    },
    {
        'id': 2,
        'name': 'Storm Kings Thunder 2',
        'players': [
            {
                'id': 1,
                'name': 'Stephanie',
                'gm': True,
                'race': None,
                'class': None
            },
            {
                'id': 2,
                'name': 'Justin',
                'gm': False,
                'race': 1,
                'class': 1
            }
        ],
        'start_date': datetime.datetime.now(),
        'status': 1
    }
]


@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    active_campaigns = [campaign for campaign in campaigns if campaign['status'] != 2]
    return jsonify({'campaign': active_campaigns})


@app.route('/campaigns/<int:campaignId>', methods=['GET'])
def get_campaign_by_id(campaign_id):
    campaign = [campaign for campaign in campaigns if campaign['id'] == campaign_id and campaign['status'] != 2]
    if len(campaign) == 0:
        abort(404)

    return jsonify({'campaign': campaign[0]})


@app.route('/campaigns', methods=['POST'])
def new_campaign():
    campaign = {
        'id': campaigns[-1]['id'] + 1,
        'name': request.json.get('name', 'New Campaign'),
        'players': request.json.get('players', []),
        'start_date': request.json.get('start_date', datetime.datetime.now()),
        'status': 1
    }
    campaigns.append(campaign)
    return jsonify({'campaign': campaign}), 201


@app.route('/campaigns/<int:campaignId>', methods=['PUT'])
def update_campaign(campaign_id):
    campaign = [campaign for campaign in campaigns if campaign['id'] == campaign_id]
    if len(campaign) == 0:
        abort(404)
    if not request.json:
        abort(400)
    # TODO: Add validators here for type
    campaign[0]['name'] = request.json.get('name', campaign[0]['name'])
    campaign[0]['players'] = request.json.get('players', campaign[0]['players'])
    campaign[0]['start_date'] = request.json.get('start_date', campaign[0]['startDate'])
    campaign[0]['status'] = request.json.get('status', campaign[0]['status'])

    return jsonify({'campaign': campaign[0]})


@app.route('/campaigns/<int:campaignId>', methods=['DELETE'])
def remove_campaign(campaign_id):
    campaign = [campaign for campaign in campaigns if campaign['id'] == campaign_id]
    if len(campaign) == 0:
        abort(404)

    campaign[0]['status'] = 2

    return jsonify({'successfullyDeleted:': campaign_id})


if __name__ == '__main__':
    app.run(debug=True)
