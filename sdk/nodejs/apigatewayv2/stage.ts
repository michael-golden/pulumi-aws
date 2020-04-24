// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages an Amazon API Gateway Version 2 stage.
 * More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html).
 * 
 * ## Example Usage
 * 
 * ### Basic
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.apigatewayv2.Stage("example", {
 *     apiId: aws_apigatewayv2_api_example.id,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/apigatewayv2_stage.html.markdown.
 */
export class Stage extends pulumi.CustomResource {
    /**
     * Get an existing Stage resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StageState, opts?: pulumi.CustomResourceOptions): Stage {
        return new Stage(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:apigatewayv2/stage:Stage';

    /**
     * Returns true if the given object is an instance of Stage.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Stage {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Stage.__pulumiType;
    }

    /**
     * Settings for logging access in this stage.
     * Use the [`aws.apigateway.Account`](https://www.terraform.io/docs/providers/aws/r/api_gateway_account.html) resource to configure [permissions for CloudWatch Logging](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#set-up-access-logging-permissions).
     */
    public readonly accessLogSettings!: pulumi.Output<outputs.apigatewayv2.StageAccessLogSettings | undefined>;
    /**
     * The API identifier.
     */
    public readonly apiId!: pulumi.Output<string>;
    /**
     * The ARN of the stage.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Whether updates to an API automatically trigger a new deployment. Defaults to `false`.
     */
    public readonly autoDeploy!: pulumi.Output<boolean | undefined>;
    /**
     * The identifier of a client certificate for the stage. Use the [`aws.apigateway.ClientCertificate`](https://www.terraform.io/docs/providers/aws/r/api_gateway_client_certificate.html) resource to configure a client certificate.
     * Supported only for WebSocket APIs.
     */
    public readonly clientCertificateId!: pulumi.Output<string | undefined>;
    /**
     * The default route settings for the stage.
     */
    public readonly defaultRouteSettings!: pulumi.Output<outputs.apigatewayv2.StageDefaultRouteSettings | undefined>;
    /**
     * The deployment identifier of the stage. Use the `aws.apigatewayv2.Deployment` resource to configure a deployment.
     */
    public readonly deploymentId!: pulumi.Output<string | undefined>;
    /**
     * The description for the stage.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The ARN prefix to be used in an [`aws.lambda.Permission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s `sourceArn` attribute
     * or in an [`aws.iam.Policy`](https://www.terraform.io/docs/providers/aws/r/iam_policy.html) to authorize access to the [`@connections` API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html).
     * See the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-control-access-iam.html) for details.
     */
    public /*out*/ readonly executionArn!: pulumi.Output<string>;
    /**
     * The URL to invoke the API pointing to the stage,
     * e.g. `wss://z4675bid1j.execute-api.eu-west-2.amazonaws.com/example-stage`
     */
    public /*out*/ readonly invokeUrl!: pulumi.Output<string>;
    /**
     * The name of the stage.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Route settings for the stage.
     */
    public readonly routeSettings!: pulumi.Output<outputs.apigatewayv2.StageRouteSetting[] | undefined>;
    /**
     * A map that defines the stage variables for the stage.
     */
    public readonly stageVariables!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * A map of tags to assign to the stage.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a Stage resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StageArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: StageArgs | StageState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as StageState | undefined;
            inputs["accessLogSettings"] = state ? state.accessLogSettings : undefined;
            inputs["apiId"] = state ? state.apiId : undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["autoDeploy"] = state ? state.autoDeploy : undefined;
            inputs["clientCertificateId"] = state ? state.clientCertificateId : undefined;
            inputs["defaultRouteSettings"] = state ? state.defaultRouteSettings : undefined;
            inputs["deploymentId"] = state ? state.deploymentId : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["executionArn"] = state ? state.executionArn : undefined;
            inputs["invokeUrl"] = state ? state.invokeUrl : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["routeSettings"] = state ? state.routeSettings : undefined;
            inputs["stageVariables"] = state ? state.stageVariables : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as StageArgs | undefined;
            if (!args || args.apiId === undefined) {
                throw new Error("Missing required property 'apiId'");
            }
            inputs["accessLogSettings"] = args ? args.accessLogSettings : undefined;
            inputs["apiId"] = args ? args.apiId : undefined;
            inputs["autoDeploy"] = args ? args.autoDeploy : undefined;
            inputs["clientCertificateId"] = args ? args.clientCertificateId : undefined;
            inputs["defaultRouteSettings"] = args ? args.defaultRouteSettings : undefined;
            inputs["deploymentId"] = args ? args.deploymentId : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["routeSettings"] = args ? args.routeSettings : undefined;
            inputs["stageVariables"] = args ? args.stageVariables : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["executionArn"] = undefined /*out*/;
            inputs["invokeUrl"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Stage.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Stage resources.
 */
export interface StageState {
    /**
     * Settings for logging access in this stage.
     * Use the [`aws.apigateway.Account`](https://www.terraform.io/docs/providers/aws/r/api_gateway_account.html) resource to configure [permissions for CloudWatch Logging](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#set-up-access-logging-permissions).
     */
    readonly accessLogSettings?: pulumi.Input<inputs.apigatewayv2.StageAccessLogSettings>;
    /**
     * The API identifier.
     */
    readonly apiId?: pulumi.Input<string>;
    /**
     * The ARN of the stage.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * Whether updates to an API automatically trigger a new deployment. Defaults to `false`.
     */
    readonly autoDeploy?: pulumi.Input<boolean>;
    /**
     * The identifier of a client certificate for the stage. Use the [`aws.apigateway.ClientCertificate`](https://www.terraform.io/docs/providers/aws/r/api_gateway_client_certificate.html) resource to configure a client certificate.
     * Supported only for WebSocket APIs.
     */
    readonly clientCertificateId?: pulumi.Input<string>;
    /**
     * The default route settings for the stage.
     */
    readonly defaultRouteSettings?: pulumi.Input<inputs.apigatewayv2.StageDefaultRouteSettings>;
    /**
     * The deployment identifier of the stage. Use the `aws.apigatewayv2.Deployment` resource to configure a deployment.
     */
    readonly deploymentId?: pulumi.Input<string>;
    /**
     * The description for the stage.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The ARN prefix to be used in an [`aws.lambda.Permission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s `sourceArn` attribute
     * or in an [`aws.iam.Policy`](https://www.terraform.io/docs/providers/aws/r/iam_policy.html) to authorize access to the [`@connections` API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html).
     * See the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-control-access-iam.html) for details.
     */
    readonly executionArn?: pulumi.Input<string>;
    /**
     * The URL to invoke the API pointing to the stage,
     * e.g. `wss://z4675bid1j.execute-api.eu-west-2.amazonaws.com/example-stage`
     */
    readonly invokeUrl?: pulumi.Input<string>;
    /**
     * The name of the stage.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Route settings for the stage.
     */
    readonly routeSettings?: pulumi.Input<pulumi.Input<inputs.apigatewayv2.StageRouteSetting>[]>;
    /**
     * A map that defines the stage variables for the stage.
     */
    readonly stageVariables?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * A map of tags to assign to the stage.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a Stage resource.
 */
export interface StageArgs {
    /**
     * Settings for logging access in this stage.
     * Use the [`aws.apigateway.Account`](https://www.terraform.io/docs/providers/aws/r/api_gateway_account.html) resource to configure [permissions for CloudWatch Logging](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#set-up-access-logging-permissions).
     */
    readonly accessLogSettings?: pulumi.Input<inputs.apigatewayv2.StageAccessLogSettings>;
    /**
     * The API identifier.
     */
    readonly apiId: pulumi.Input<string>;
    /**
     * Whether updates to an API automatically trigger a new deployment. Defaults to `false`.
     */
    readonly autoDeploy?: pulumi.Input<boolean>;
    /**
     * The identifier of a client certificate for the stage. Use the [`aws.apigateway.ClientCertificate`](https://www.terraform.io/docs/providers/aws/r/api_gateway_client_certificate.html) resource to configure a client certificate.
     * Supported only for WebSocket APIs.
     */
    readonly clientCertificateId?: pulumi.Input<string>;
    /**
     * The default route settings for the stage.
     */
    readonly defaultRouteSettings?: pulumi.Input<inputs.apigatewayv2.StageDefaultRouteSettings>;
    /**
     * The deployment identifier of the stage. Use the `aws.apigatewayv2.Deployment` resource to configure a deployment.
     */
    readonly deploymentId?: pulumi.Input<string>;
    /**
     * The description for the stage.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the stage.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Route settings for the stage.
     */
    readonly routeSettings?: pulumi.Input<pulumi.Input<inputs.apigatewayv2.StageRouteSetting>[]>;
    /**
     * A map that defines the stage variables for the stage.
     */
    readonly stageVariables?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * A map of tags to assign to the stage.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
