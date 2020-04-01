// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides a DMS (Data Migration Service) endpoint resource. DMS endpoints can be created, updated, deleted, and imported.
 * 
 * > **Note:** All arguments including the password will be stored in the raw state as plain-text.
 * [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * // Create a new endpoint
 * const test = new aws.dms.Endpoint("test", {
 *     certificateArn: "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012",
 *     databaseName: "test",
 *     endpointId: "test-dms-endpoint-tf",
 *     endpointType: "source",
 *     engineName: "aurora",
 *     extraConnectionAttributes: "",
 *     kmsKeyArn: "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
 *     password: "test",
 *     port: 3306,
 *     serverName: "test",
 *     sslMode: "none",
 *     tags: {
 *         Name: "test",
 *     },
 *     username: "test",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dms_endpoint.html.markdown.
 */
export class Endpoint extends pulumi.CustomResource {
    /**
     * Get an existing Endpoint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EndpointState, opts?: pulumi.CustomResourceOptions): Endpoint {
        return new Endpoint(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:dms/endpoint:Endpoint';

    /**
     * Returns true if the given object is an instance of Endpoint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Endpoint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Endpoint.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) for the certificate.
     */
    public readonly certificateArn!: pulumi.Output<string>;
    /**
     * The name of the endpoint database.
     */
    public readonly databaseName!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) for the endpoint.
     */
    public /*out*/ readonly endpointArn!: pulumi.Output<string>;
    /**
     * The database endpoint identifier.
     */
    public readonly endpointId!: pulumi.Output<string>;
    /**
     * The type of endpoint. Can be one of `source | target`.
     */
    public readonly endpointType!: pulumi.Output<string>;
    /**
     * The type of engine for the endpoint. Can be one of `aurora | azuredb | db2 | docdb | dynamodb | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.
     */
    public readonly engineName!: pulumi.Output<string>;
    /**
     * Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).
     */
    public readonly extraConnectionAttributes!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kmsKeyArn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
     */
    public readonly kmsKeyArn!: pulumi.Output<string>;
    /**
     * Settings for the source MongoDB endpoint. Available settings are `authType` (default: `password`), `authMechanism` (default: `default`), `nestingLevel` (default: `none`), `extractDocId` (default: `false`), `docsToInvestigate` (default: `1000`) and `authSource` (default: `admin`). For more details, see [Using MongoDB as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html).
     */
    public readonly mongodbSettings!: pulumi.Output<outputs.dms.EndpointMongodbSettings | undefined>;
    /**
     * The password to be used to login to the endpoint database.
     */
    public readonly password!: pulumi.Output<string | undefined>;
    /**
     * The port used by the endpoint database.
     */
    public readonly port!: pulumi.Output<number | undefined>;
    /**
     * Settings for the target S3 endpoint. Available settings are `serviceAccessRoleArn`, `externalTableDefinition`, `csvRowDelimiter` (default: `\\n`), `csvDelimiter` (default: `,`), `bucketFolder`, `bucketName` and `compressionType` (default: `NONE`). For more details, see [Using Amazon S3 as a Target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html).
     */
    public readonly s3Settings!: pulumi.Output<outputs.dms.EndpointS3Settings | undefined>;
    /**
     * The host name of the server.
     */
    public readonly serverName!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.
     */
    public readonly serviceAccessRole!: pulumi.Output<string | undefined>;
    /**
     * The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`
     */
    public readonly sslMode!: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * The user name to be used to login to the endpoint database.
     */
    public readonly username!: pulumi.Output<string | undefined>;

    /**
     * Create a Endpoint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: EndpointArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: EndpointArgs | EndpointState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as EndpointState | undefined;
            inputs["certificateArn"] = state ? state.certificateArn : undefined;
            inputs["databaseName"] = state ? state.databaseName : undefined;
            inputs["endpointArn"] = state ? state.endpointArn : undefined;
            inputs["endpointId"] = state ? state.endpointId : undefined;
            inputs["endpointType"] = state ? state.endpointType : undefined;
            inputs["engineName"] = state ? state.engineName : undefined;
            inputs["extraConnectionAttributes"] = state ? state.extraConnectionAttributes : undefined;
            inputs["kmsKeyArn"] = state ? state.kmsKeyArn : undefined;
            inputs["mongodbSettings"] = state ? state.mongodbSettings : undefined;
            inputs["password"] = state ? state.password : undefined;
            inputs["port"] = state ? state.port : undefined;
            inputs["s3Settings"] = state ? state.s3Settings : undefined;
            inputs["serverName"] = state ? state.serverName : undefined;
            inputs["serviceAccessRole"] = state ? state.serviceAccessRole : undefined;
            inputs["sslMode"] = state ? state.sslMode : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["username"] = state ? state.username : undefined;
        } else {
            const args = argsOrState as EndpointArgs | undefined;
            if (!args || args.endpointId === undefined) {
                throw new Error("Missing required property 'endpointId'");
            }
            if (!args || args.endpointType === undefined) {
                throw new Error("Missing required property 'endpointType'");
            }
            if (!args || args.engineName === undefined) {
                throw new Error("Missing required property 'engineName'");
            }
            inputs["certificateArn"] = args ? args.certificateArn : undefined;
            inputs["databaseName"] = args ? args.databaseName : undefined;
            inputs["endpointId"] = args ? args.endpointId : undefined;
            inputs["endpointType"] = args ? args.endpointType : undefined;
            inputs["engineName"] = args ? args.engineName : undefined;
            inputs["extraConnectionAttributes"] = args ? args.extraConnectionAttributes : undefined;
            inputs["kmsKeyArn"] = args ? args.kmsKeyArn : undefined;
            inputs["mongodbSettings"] = args ? args.mongodbSettings : undefined;
            inputs["password"] = args ? args.password : undefined;
            inputs["port"] = args ? args.port : undefined;
            inputs["s3Settings"] = args ? args.s3Settings : undefined;
            inputs["serverName"] = args ? args.serverName : undefined;
            inputs["serviceAccessRole"] = args ? args.serviceAccessRole : undefined;
            inputs["sslMode"] = args ? args.sslMode : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["username"] = args ? args.username : undefined;
            inputs["endpointArn"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Endpoint.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Endpoint resources.
 */
export interface EndpointState {
    /**
     * The Amazon Resource Name (ARN) for the certificate.
     */
    readonly certificateArn?: pulumi.Input<string>;
    /**
     * The name of the endpoint database.
     */
    readonly databaseName?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) for the endpoint.
     */
    readonly endpointArn?: pulumi.Input<string>;
    /**
     * The database endpoint identifier.
     */
    readonly endpointId?: pulumi.Input<string>;
    /**
     * The type of endpoint. Can be one of `source | target`.
     */
    readonly endpointType?: pulumi.Input<string>;
    /**
     * The type of engine for the endpoint. Can be one of `aurora | azuredb | db2 | docdb | dynamodb | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.
     */
    readonly engineName?: pulumi.Input<string>;
    /**
     * Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).
     */
    readonly extraConnectionAttributes?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kmsKeyArn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
     */
    readonly kmsKeyArn?: pulumi.Input<string>;
    /**
     * Settings for the source MongoDB endpoint. Available settings are `authType` (default: `password`), `authMechanism` (default: `default`), `nestingLevel` (default: `none`), `extractDocId` (default: `false`), `docsToInvestigate` (default: `1000`) and `authSource` (default: `admin`). For more details, see [Using MongoDB as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html).
     */
    readonly mongodbSettings?: pulumi.Input<inputs.dms.EndpointMongodbSettings>;
    /**
     * The password to be used to login to the endpoint database.
     */
    readonly password?: pulumi.Input<string>;
    /**
     * The port used by the endpoint database.
     */
    readonly port?: pulumi.Input<number>;
    /**
     * Settings for the target S3 endpoint. Available settings are `serviceAccessRoleArn`, `externalTableDefinition`, `csvRowDelimiter` (default: `\\n`), `csvDelimiter` (default: `,`), `bucketFolder`, `bucketName` and `compressionType` (default: `NONE`). For more details, see [Using Amazon S3 as a Target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html).
     */
    readonly s3Settings?: pulumi.Input<inputs.dms.EndpointS3Settings>;
    /**
     * The host name of the server.
     */
    readonly serverName?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.
     */
    readonly serviceAccessRole?: pulumi.Input<string>;
    /**
     * The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`
     */
    readonly sslMode?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The user name to be used to login to the endpoint database.
     */
    readonly username?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Endpoint resource.
 */
export interface EndpointArgs {
    /**
     * The Amazon Resource Name (ARN) for the certificate.
     */
    readonly certificateArn?: pulumi.Input<string>;
    /**
     * The name of the endpoint database.
     */
    readonly databaseName?: pulumi.Input<string>;
    /**
     * The database endpoint identifier.
     */
    readonly endpointId: pulumi.Input<string>;
    /**
     * The type of endpoint. Can be one of `source | target`.
     */
    readonly endpointType: pulumi.Input<string>;
    /**
     * The type of engine for the endpoint. Can be one of `aurora | azuredb | db2 | docdb | dynamodb | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.
     */
    readonly engineName: pulumi.Input<string>;
    /**
     * Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).
     */
    readonly extraConnectionAttributes?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kmsKeyArn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
     */
    readonly kmsKeyArn?: pulumi.Input<string>;
    /**
     * Settings for the source MongoDB endpoint. Available settings are `authType` (default: `password`), `authMechanism` (default: `default`), `nestingLevel` (default: `none`), `extractDocId` (default: `false`), `docsToInvestigate` (default: `1000`) and `authSource` (default: `admin`). For more details, see [Using MongoDB as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html).
     */
    readonly mongodbSettings?: pulumi.Input<inputs.dms.EndpointMongodbSettings>;
    /**
     * The password to be used to login to the endpoint database.
     */
    readonly password?: pulumi.Input<string>;
    /**
     * The port used by the endpoint database.
     */
    readonly port?: pulumi.Input<number>;
    /**
     * Settings for the target S3 endpoint. Available settings are `serviceAccessRoleArn`, `externalTableDefinition`, `csvRowDelimiter` (default: `\\n`), `csvDelimiter` (default: `,`), `bucketFolder`, `bucketName` and `compressionType` (default: `NONE`). For more details, see [Using Amazon S3 as a Target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html).
     */
    readonly s3Settings?: pulumi.Input<inputs.dms.EndpointS3Settings>;
    /**
     * The host name of the server.
     */
    readonly serverName?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.
     */
    readonly serviceAccessRole?: pulumi.Input<string>;
    /**
     * The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`
     */
    readonly sslMode?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The user name to be used to login to the endpoint database.
     */
    readonly username?: pulumi.Input<string>;
}
