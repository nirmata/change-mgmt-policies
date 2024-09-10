This is a demo repository to scan CloudFormation templates. The scanned results can be viewed via the Nirmata Policy Manager.

The GitHub Action converts the CDK file into a CloudFormation template using the `cdk synth` command. The policies are applied on the generated JSON file. The results are then published to the Nirmata Policy Manager (NPM).
